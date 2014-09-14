# based on PLD Linux spec git://git.pld-linux.org/packages/acl.git
Summary:	Utilities for managing
Name:		acl
Version:	2.2.52
Release:	3
License:	LGPL v2+ (library), GPL v2 (utilities)
Group:		Core/System
Source0:	http://download.savannah.gnu.org/releases/acl/%{name}-%{version}.src.tar.gz
# Source0-md5:	a61415312426e9c2212bd7dc7929abda
URL:		http://savannah.nongnu.org/projects/acl
BuildRequires:	attr-devel
BuildRequires:	gettext
BuildRequires:	libtool
Requires:	attr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of tools for manipulating ACL on filesystem objects.

%package devel
Summary:	Header files and libraries for acl development
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and libraries needed to develop programs which make use
of access control lists.

%prep
%setup -q

%build
%{__libtoolize}
%configure \
	--disable-static
%{__make} \
	DEBUG="-DNDEBUG"	\
	OPTIMIZER="%{rpmcflags} -DENABLE_GETTEXT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/acl,%{_mandir}/man3}

%{__make} install install-lib install-dev \
	DIST_ROOT=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/{acl_copy_int,acl_set_fd,acl_set_file,acl_to_text}.3

echo ".so acl_copy_ext.3"  > $RPM_BUILD_ROOT%{_mandir}/man3/acl_copy_int.3
echo ".so acl_get_fd.3"    > $RPM_BUILD_ROOT%{_mandir}/man3/acl_set_fd.3
echo ".so acl_get_file.3"  > $RPM_BUILD_ROOT%{_mandir}/man3/acl_set_file.3
echo ".so acl_from_text.3" > $RPM_BUILD_ROOT%{_mandir}/man3/acl_to_short_text.3
echo ".so acl_from_text.3" > $RPM_BUILD_ROOT%{_mandir}/man3/acl_to_text.3

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README doc/{CHANGES,TODO}
%attr(755,root,root) %{_bindir}/chacl
%attr(755,root,root) %{_bindir}/getfacl
%attr(755,root,root) %{_bindir}/setfacl
%attr(755,root,root) %ghost %{_libdir}/libacl.so.?
%attr(755,root,root) %{_libdir}/libacl.so.*.*.*
%{_mandir}/man1/chacl.1*
%{_mandir}/man1/getfacl.1*
%{_mandir}/man1/setfacl.1*
%{_mandir}/man5/acl.5*

%files devel
%defattr(644,root,root,755)
%doc doc/{extensions.txt,libacl.txt}
%attr(755,root,root) %{_libexecdir}/libacl.so
%{_libexecdir}/libacl.la
%{_includedir}/acl
%{_includedir}/sys/acl.h
%{_mandir}/man3/acl_*.3*

