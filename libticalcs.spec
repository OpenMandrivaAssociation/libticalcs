%define oname libticalcs2
%define version 1.1.7
%define release 2


%define libticables_version 1.3.3
%define libtifiles_version 1.1.5

%define major 10
%define libname %mklibname ticalcs %{major}
%define develname %mklibname -d ticalcs

Summary:	Library to handle the different TI calculators
Name:		libticalcs
Version:	%{version}
Release:	%{release}
Epoch:		1
License:	LGPLv2+
Group:		Communications
URL:		https://tilp.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/tilp/%{oname}-%{version}.tar.bz2 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libticables-devel >= %{libticables_version}
BuildRequires:	libtifiles-devel >= %{libtifiles_version}

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
# %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc




%changelog
* Thu Jan 19 2012 Zombie Ryushu <ryushu@mandriva.org> 1:1.1.7-1mdv2012.0
+ Revision: 762269
- Fix libs
- Fix libs

* Tue Jul 13 2010 Zombie Ryushu <ryushu@mandriva.org> 1:1.1.5-1mdv2011.0
+ Revision: 551880
- Upgrade and fix dependencies
- Upgrade to 1.3.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Mar 12 2009 Olivier Thauvin <nanardon@mandriva.org> 1:1.1.2-6mdv2009.1
+ Revision: 354064
- rebuild

* Mon Feb 23 2009 Zombie Ryushu <ryushu@mandriva.org> 1:1.1.2-5mdv2009.1
+ Revision: 344162
- Remove circular requirement

* Mon Feb 23 2009 Zombie Ryushu <ryushu@mandriva.org> 1:1.1.2-4mdv2009.1
+ Revision: 344148
- Increment release
- Remove circular requirement
- Remove redundant redefine of epoch
- Add epoch to requirements

* Sun Feb 22 2009 Zombie Ryushu <ryushu@mandriva.org> 1:1.1.2-3mdv2009.1
+ Revision: 343891
- Bump Release
- Fix circular dependancy in Devel package

* Sun Feb 22 2009 Zombie Ryushu <ryushu@mandriva.org> 1:1.1.2-2mdv2009.1
+ Revision: 343792
- Fix find_lang

* Sun Feb 22 2009 Zombie Ryushu <ryushu@mandriva.org> 1:1.1.2-1mdv2009.1
+ Revision: 343786
- Fixed Lang Package temporarily and updated to 1.1.2
- Fixed Lang Package temporarily and updated to 1.1.2
- Fixed Lang Package temporarily and updated to 1.1.2

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 4.6.2-5mdv2009.0
+ Revision: 268035
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jun 07 2008 Funda Wang <fwang@mandriva.org> 4.6.2-4mdv2009.0
+ Revision: 216577
- fix conflicts with libticables

* Tue Mar 25 2008 Emmanuel Andry <eandry@mandriva.org> 4.6.2-3mdv2008.1
+ Revision: 189888
- Fix lib group
- protect major

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Funda Wang <fwang@mandriva.org> 4.6.2-2mdv2008.1
+ Revision: 116807
- New devel package policy


* Sun Jan 21 2007 Olivier Thauvin <nanardon@mandriva.org> 4.6.2-1mdv2007.0
+ Revision: 111423
- 4.6.2
- 4.6.1
- Import libticalcs

* Wed Jun 29 2005 Olivier Thauvin <nanardon@mandriva.org> 4.5.9-1mdk
- 4.5.9

* Sun Feb 06 2005 Abel Cheung <deaddog@mandrake.org> 4.5.5-1mdk
- New version
- Split package, otherwise can't have multilib

* Mon May 31 2004 Abel Cheung <deaddog@deaddog.org> 4.5.3-1mdk
- New version
- Doesn't need to build against multiple version of glib, thus change
  package name back to old one

