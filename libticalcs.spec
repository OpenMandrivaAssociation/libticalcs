%define version 4.6.2
%define release %mkrel 1

%define libticables_version 3.6.1
%define libtifiles_version 0.6.1

%define major 4
%define libname %mklibname ticalcs %{major}

Summary:	Library to handle the different TI calculators
Name:		libticalcs
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Communications
URL:		http://tilp.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/tilp/%{name}-%{version}.tar.bz2 
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
Group:		Communications
Provides:	%{name} = %{version}-%{release}
Requires:	%{name} = %{version}

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


%package	-n %{libname}-devel
Summary:	Development related files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	libticables-devel >= %{libticables_version}
Requires:	libtifiles-devel >= %{libtifiles_version}

%description	-n %{libname}-devel
This package contains headers and other necessary files to develop 
or compile applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x --enable-static=yes
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std gnulocaledir=${RPM_BUILD_ROOT}%{_datadir}/locale

%find_lang %{name}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -f %{name}.lang
%defattr(-,root,root)

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_includedir}/tilp/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc



