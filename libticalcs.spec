%define oname libticalcs2
%define version 1.1.2
%define release %mkrel 1


%define libticables_version 1.2.0
%define libtifiles_version 1.1.1

%define major 7
%define libname %mklibname ticalcs %{major}
%define develname %mklibname -d ticalcs

Summary:	Library to handle the different TI calculators
Name:		libticalcs
Version:	%{version}
Release:	%{release}
Epoch:		1
License:	LGPLv2+
Group:		Communications
URL:		http://tilp.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/tilp/%{oname}-%{version}.tar.bz2 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libticables-devel >= %{libticables_version}
BuildRequires:	libtifiles-devel >= %{libtifiles_version}
Requires:	%{libname} = %{version}

%description
The TiCalcs library is a part of the TiLP project and constitutes with
the other libraries a complete framework for developping and/or linking
TI files oriented applications.

It is a library which brings about all the functions needed to communicate
with a Texas Instruments graphing calculator (or hand-held), without
worrying about packet oriented protocol, the file management and some
other stuffs. Currently, it does not support some education devices
(such as CBL/CBR and others).

It supports all currently available calculators and their associated file
formats:
- TI8x calculators: TI73, 82, 83, TI83+, 85 and 86 (with 2 sub-classes:
  TI73/83+ and 85/86).
- TI9x calculators: TI89, 92, 92+ and V200PLT.

%package	-n %{libname}
Summary:	Library to handle different TI calculators
Group:		System/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	-n %{libname}
The TiCalcs library is a part of the TiLP project and constitutes with
the other libraries a complete framework for developping and/or linking
TI files oriented applications.

It is a library which brings about all the functions needed to communicate
with a Texas Instruments graphing calculator (or hand-held), without
worrying about packet oriented protocol, the file management and some
other stuffs. Currently, it does not support some education devices
(such as CBL/CBR and others).

It supports all currently available calculators and their associated file
formats:
- TI8x calculators: TI73, 82, 83, TI83+, 85 and 86 (with 2 sub-classes:
  TI73/83+ and 85/86).
- TI9x calculators: TI89, 92, 92+ and V200PLT.


%package	-n %{develname}
Summary:	Development related files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d ticalcs 4

%description	-n %{develname}
This package contains headers and other necessary files to develop 
or compile applications that use %{name}.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x --enable-static=yes
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std gnulocaledir=%{buildroot}%{_datadir}/locale

#fix conflicts with libticables-devel
rm -f %buildroot%_includedir/tilp/export.h

%find_lang %{oname}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -f %{oname}.lang
%defattr(-,root,root)

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_includedir}/tilp2/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
